# SS Subscription to Configuration Files

Simple Python script for converting Shadowsocks SIP008 subscription to
[Shadowsock-Rust][ss-rust]'s `sslocal` (*config,json*)
and [shadowsocks-windows-gui-rust][russ]'s `russ` (*russ.json*)
configuration file.

[ss-rust]: https://github.com/shadowsocks/shadowsocks-rust
[russ]: https://github.com/cg31/shadowsocks-windows-gui-rust

**Notice**:

`sslocal` run as a socks5 server by default. Unfortunately, Socks5 support on Windows varies between applications. One may find useful adding `"protocol": "http"` to *config.json*.

```json
{
  "protocol": "http",
  "local_address": "127.0.0.1",
  "local_port": 1080,
}
```
