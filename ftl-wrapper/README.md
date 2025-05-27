# FTL Wrapper
---
| This directory contains all things related to the wrapper that will extend the FTL between SSDs and cart

PCIe: Peripherial Component Interconnect (Express)
- connects expansion cards (storage controllers) to the motherboard
- come in "lanes" (sizes):= # data lanes available for communication
- different size: x2, x4, x8, x16, x32 (bidirectional data transfer)
    - x1 slot can move data @ rate: 1 bit / cycle
    - x2 rate: 2 bits / cycle, etc.
- for us: PCIe x4: standard size for storage controllers

PCIe card: expansion card that connects computer's motherboard using a PCIe slot
- in our case, we likely have a Storage Controller Card
- ASIC (Application-Specific Integrated Circuit), handles communication with the NAND flash memory, error correction, wear leveling, and more critical functions
- connects to host through "serial" link => not over a shared bus (P2P architecture)

PCIe Lane: single data channel with PCIe slot/connection
- Tx & Rx pairs work to transmit data
- \> 1 lane => higher transfer rate = better performance
- assume we use PCIe Gen >= 4

Limitations:
- Each combo of processor and chipset: **limited** number of PCIe lanes
- lines divided between CPU/chipset links (depends on motherboard)

Batch Size: Assume 1 100GB for now / batch size
Optimal Batch Size: TBD

Modern SSDs facts (SLC):
- R/W in pages, delete data in "blocks"
- 1 page ~ 8192 bytes (2x4096)
- 1 block ~ 256 pages (2097152 bytes OR ~ 2 MB)
- Write: copy data to cache, eraser block, rewrite entire block elsewhere

**SSD's controller** - a processor that provides the interface between the SSD and the host and that handles all of the decisions about what gets written to which NAND chips and how—has multiple channels it can use to address its attached NAND chips
- writes and reads data in stripes across its NAND chips
- method similar to traditional multi-hard disk RAID
- M key configuration for PCI-Express drives (NVMe protocol)
- 3D-NAND = V-NAND (stacking memory cells vertically, reduces wear/tear)

## NVMe Command Line Tool
---
- https://github.com/linux-nvme/nvme-cli (there exists a manpage for this for [Linux](https://manpages.debian.org/testing/nvme-cli/nvme.1.en.html))
    - NVM-Express is a fast, scalable host controller interface designed to address the needs for not only PCI Express based solid state drives
- `nvme <command> <device> [<args>]`
- List of built in commands added in: https://github.com/linux-nvme/nvme-cli/blob/master/nvme-builtin.h
- say we do a READ, then callback is
```
static int read_cmd(int argc, char **argv, struct command *cmd, struct plugin *plugin)
{
	const char *desc = "Copy specified logical blocks on the given\n"
		"device to specified data buffer (default buffer is stdout).";

	return submit_io(nvme_cmd_read, "read", desc, argc, argv);
}

We have a config struct:
struct config {
		__u32	namespace_id;
		__u64	start_block;
		__u16	block_count;
		__u64	data_size;
		__u64	metadata_size;
		__u64	ref_tag;
		char	*data;
		char	*metadata;
		__u8	prinfo;
		__u16	app_tag_mask;
		__u16	app_tag;
		__u64	storage_tag;
		bool	limited_retry;
		bool	force_unit_access;
		bool	storage_tag_check;
		__u8	dtype;
		__u16	dspec;
		__u8	dsmgmt;
		bool	show;
		bool	latency;
		bool	force;
	};

submit_io definition:
static int submit_io(int opcode, char *command, const char *desc, int argc, char **argv)
{
	...
	declaration/initialization of variables + the following:
	const char *start_block_addr = "64-bit addr of first block to access";
	const char *data_size = "size of data in bytes";
	const char *metadata_size = "size of metadata in bytes";
	const char *data = "data file";
	const char *metadata = "metadata file";
	const char *limited_retry_num = "limit num. media access attempts";
	const char *show = "show command before sending";
	const char *dtype_for_write = "directive type (for write-only)";
	const char *dspec = "directive specific (for write-only)";
	const char *dsm = "dataset management attributes (lower 8 bits)";
	const char *storage_tag_check = "This bit specifies the Storage Tag field shall be\n"
		                            "checked as part of end-to-end data protection processing";
	const char *force = "The \"I know what I'm doing\" flag, do not enforce exclusive access for write";

	struct config cfg = {
		.namespace_id		= 0,
		.start_block		= 0,
		.block_count		= 0,
		.data_size		    = 0,
		.metadata_size		= 0,
		.ref_tag		    = 0,
		.data			    = "",
		.metadata		    = "",
		.prinfo			    = 0,
		.app_tag_mask		= 0,
		.app_tag		    = 0,
		.storage_tag		= 0,
		.limited_retry		= false,
		.force_unit_access	= false,
		.storage_tag_check	= false,
		.dtype			    = 0,
		.dspec			    = 0,
		.dsmgmt			    = 0,
		.show			    = false,
		.latency		    = false,
		.force			    = false,
	};

	NVME_ARGS(opts,
		  OPT_UINT("namespace-id",      'n', &cfg.namespace_id,      namespace_id_desired),
		  OPT_SUFFIX("start-block",     's', &cfg.start_block,       start_block_addr),
		  OPT_SHRT("block-count",       'c', &cfg.block_count,       block_count),
		  OPT_SUFFIX("data-size",       'z', &cfg.data_size,         data_size),
		  OPT_SUFFIX("metadata-size",   'y', &cfg.metadata_size,     metadata_size),
		  OPT_SUFFIX("ref-tag",         'r', &cfg.ref_tag,           ref_tag),
		  OPT_FILE("data",              'd', &cfg.data,              data),
		  OPT_FILE("metadata",          'M', &cfg.metadata,          metadata),
		  OPT_BYTE("prinfo",            'p', &cfg.prinfo,            prinfo),
		  OPT_SHRT("app-tag-mask",      'm', &cfg.app_tag_mask,      app_tag_mask),
		  OPT_SHRT("app-tag",           'a', &cfg.app_tag,           app_tag),
		  OPT_SUFFIX("storage-tag",     'g', &cfg.storage_tag,       storage_tag),
		  OPT_FLAG("limited-retry",     'l', &cfg.limited_retry,     limited_retry_num),
		  OPT_FLAG("force-unit-access", 'f', &cfg.force_unit_access, force_unit_access),
		  OPT_FLAG("storage-tag-check", 'C', &cfg.storage_tag_check, storage_tag_check),
		  OPT_BYTE("dir-type",          'T', &cfg.dtype,             dtype_for_write),
		  OPT_SHRT("dir-spec",          'S', &cfg.dspec,             dspec),
		  OPT_BYTE("dsm",               'D', &cfg.dsmgmt,            dsm),
		  OPT_FLAG("show-command",      'V', &cfg.show,              show),
		  OPT_FLAG("dry-run",           'w', &nvme_cfg.dry_run,      dry_run),
		  OPT_FLAG("latency",           't', &cfg.latency,           latency),
		  OPT_FLAG("force",              0 , &cfg.force,             force));

	if (opcode != nvme_cmd_write) {
		err = parse_and_open(&dev, argc, argv, desc, opts); 
        // calls "static int get_dev(struct nvme_dev **dev, int argc, char **argv, int flags)"
	} else { // handle opcode == nvme_cmd_write }

	err = nvme_get_nsid(dev_fd(dev), &cfg.namespace_id);
    // Retrieve the NSID from a namespace file descriptor

	...some control logic here...

	if (opcode & 1) { // READ
		dfd = mfd = STDIN_FILENO;
		flags = O_RDONLY;
	}
	if (strlen(cfg.data)) {
		dfd = open(cfg.data, flags, mode);
	}
	if (strlen(cfg.metadata)) {
		mfd = open(cfg.metadata, flags, mode);
	}
	ns = nvme_alloc(sizeof(*ns));
	err = nvme_cli_identify_ns(dev, cfg.namespace_id, ns);
    // identify and retrieve information about a namespace on an NVMe device

	nvme_id_ns_flbas_to_lbaf_inuse(ns->flbas, &lba_index);
    // convert the value of the flbas (Formatted LBA Size) field => idx of LBA Format (LBAF) "in use" by namespace

	logical_block_size = 1 << ns->lbaf[lba_index].ds;
	ms = le16_to_cpu(ns->lbaf[lba_index].ms);
	nvm_ns = nvme_alloc(sizeof(*nvm_ns));

	err = nvme_identify_ns_csi(dev_fd(dev), cfg.namespace_id, 0, NVME_CSI_NVM, nvm_ns);
    // identify a namespace with respect to a specific Command Set Identifier (CSI)
	if (!err) {get_pif_sts(ns, nvm_ns, &pif, &sts);}
	pi_size = (pif == NVME_NVM_PIF_16B_GUARD) ? 8 : 16;
	if (NVME_FLBAS_META_EXT(ns->flbas)) {
		if (!((cfg.prinfo & 0x8) != 0 && ms == pi_size))
			logical_block_size += ms;
	}

	buffer_size = ((long long)cfg.block_count + 1) * logical_block_size;
	buffer_size = cfg.data_size;

    // allocate buffer based on # blocks needed
	if (argconfig_parse_seen(opts, "block-count")) {
		/* Use the value provided */
		nblocks = cfg.block_count;
	} else {
		/* Get the required block count. Note this is a zeroes based value. */
		nblocks = ((buffer_size + (logical_block_size - 1)) / logical_block_size) - 1;

		/* Update the data size based on the required block count */
		buffer_size = ((unsigned long long)nblocks + 1) * logical_block_size;
	}
	buffer = nvme_alloc_huge(buffer_size, &mh);

	if (cfg.metadata_size) {
		mbuffer_size = ((unsigned long long)cfg.block_count + 1) * ms;
		mbuffer_size = cfg.metadata_size;
		mbuffer = malloc(mbuffer_size);
		memset(mbuffer, 0, mbuffer_size);
	}

	if (opcode & 1) { err = read(dfd, (void *)buffer, cfg.data_size); // reads the data }

	if ((opcode & 1) && cfg.metadata_size) { err = read(mfd, (void *)mbuffer, mbuffer_size); }

	... some extra lines we don't need to know happens here ...
	struct nvme_io_args args = {
		.args_size	= sizeof(args),
		.fd		= dev_fd(dev),
		.nsid		= cfg.namespace_id,
		.slba		= cfg.start_block,
		.nlb		= nblocks,
		.control	= control,
		.dsm		= cfg.dsmgmt,
		.sts		= sts,
		.pif		= pif,
		.dspec		= cfg.dspec,
		.reftag		= (__u32)cfg.ref_tag,
		.reftag_u64	= cfg.ref_tag,
		.apptag		= cfg.app_tag,
		.appmask	= cfg.app_tag_mask,
		.storage_tag	= cfg.storage_tag,
		.data_len	= buffer_size,
		.data		= buffer,
		.metadata_len	= mbuffer_size,
		.metadata	= mbuffer,
		.timeout	= nvme_cfg.timeout,
		.result		= NULL,
	};
    
	err = nvme_io(&args, opcode);
	return err;
}
```

## What "client" needs to know (at minimum)
---
- cmd: `nvme read /dev/nvme0n1 --namespace-id=<nsid> --start-block=<slba> --block-count=<nblocks> --data=<output_file>`
- to know: devname [/dev/nvme0n1], namespace_id [nsid], start_block [slba], block_count [nblocks], data [output_file]
    - note: block_count = 0 := read 1 block
    - note: output_file will be the fd that "client" opens as standard out
    - note: typically namespace=1 else try `nvme list`
        - typically in LINUX, they appear as separate devices
            - `/dev/nvme0n1 → namespace 1`
            - `/dev/nvme0n2 → namespace 2`
    - note: example on how to find namespace, `nvme id-ns [devname] --namespace-id=[nsid]`
        - output: `lba data size   : 512`
- computation on how many blocks to read: 
    - Given: block_size (constant), data_size (input), offset
    - `start_block` = offset / block_size **IMPORTANT, USER STORES OFFSET**
        - app/higher-level software knows where data is located
        - uses a key-value store backed by raw NVMe [map keys to fixed block regions]
    - `block-count` = ceil(data_size / block_size) - 1

## What "server" needs to hash
---
- Data Chunk ID	
- NVMe Device	
- Namespace ID	
- Start Block	Block Coun

## More on PCIe lanes
---
- [ ] Figure out how many PCI lanes can we do at a single time for each server/cart?
- [ ] Server uses: PCIe addressing (Bus/Device/Function)