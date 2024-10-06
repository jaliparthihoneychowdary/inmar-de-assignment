package utils

object keyValueStoreUtil {

    private var store = Map[String, String]()

    def put(key: String, value: String): Unit = {
      if (store.contains(key)) {
        println(s"Info: Key '$key' already exists. Overwriting the value.")
      }
      store += (key -> value)
    }

    def get(key: String): Option[String] = {
      store.get(key) match {
        case Some(_) => store.get(key)
        case None =>
          println(s"Warn: Key '$key' does not exist.")
          None
      }

    }

    def remove(key: String): Option[String] = {
      store.get(key) match {
        case Some(_) =>
          val value = store.get(key)
          store -= key
          value
        case None =>
          println(s"Warn: Key '$key' does not exist.")
          None
      }
    }

    def keys(): List[String] = {
      store.keys.toList
    }
}
