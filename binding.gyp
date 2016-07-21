{
  "targets": [
    {
      "target_name": "msg",
      "sources": [ "src/msg.cc", "src/functions.cc" ],
      "cflags_cc": [ "-std=c++0x" ],
      "include_dirs" : [
        "<!(node -e \"require('nan')\")"
      ]
    }
  ]
}
