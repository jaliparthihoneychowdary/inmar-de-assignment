package main

import utils.keyValueStoreUtil

object keyValueStoreMain {

    def main(args: Array[String]): Unit = {
      keyValueStoreUtil.put("key1", "value1")
      println(keyValueStoreUtil.get("key1"))

      keyValueStoreUtil.put("key2", "value2")
      println(keyValueStoreUtil.keys())

      println(keyValueStoreUtil.remove("key2"))
      println(keyValueStoreUtil.keys())
    }

}
