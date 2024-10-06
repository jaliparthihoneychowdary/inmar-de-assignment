import org.scalatest.funsuite.AnyFunSuite
import utils.keyValueStoreUtil

object keyValueStoreUtilTest extends AnyFunSuite {


    test("put should store a key-value pair and get should retrieve the correct value") {
      keyValueStoreUtil.put("key1", "value1")
      assert(keyValueStoreUtil.get("key1").contains("value1"))
    }

    test("get should return None for a non-existent key") {
      assert(keyValueStoreUtil.get("nonExistentKey").isEmpty)
    }

    test("remove should delete a key-value pair and return the removed value") {
      keyValueStoreUtil.put("key2", "value2")
      assert(keyValueStoreUtil.remove("key2").contains("value2"))
      assert(keyValueStoreUtil.get("key2").isEmpty)
    }

    test("remove should return None if the key does not exist") {
      assert(keyValueStoreUtil.remove("nonExistentKey").isEmpty)
    }

    test("keys should return a list of all keys in the store") {
      keyValueStoreUtil.put("key3", "value3")
      keyValueStoreUtil.put("key4", "value4")
      val keysList = keyValueStoreUtil.keys()
      assert(keysList.contains("key3"))
      assert(keysList.contains("key4"))
    }

    test("keys should return an empty list when the store is empty") {
      keyValueStoreUtil.remove("key3")
      keyValueStoreUtil.remove("key4")
      assert(keyValueStoreUtil.keys().isEmpty)
    }


}
