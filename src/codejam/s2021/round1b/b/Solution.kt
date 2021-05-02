package codejam.s2021.round1b.b

import java.io.BufferedReader
import java.io.InputStream
import java.io.InputStreamReader
import java.io.PrintStream
import java.util.*

fun main() {
    solve(System.`in`, System.out)
}

fun solve(inputStream: InputStream, out: PrintStream) {
    val reader = BufferedReader(InputStreamReader(inputStream))
    val printer = PrintStream(out)
    val readLine = { reader.readLine() }
    val println = { it: String -> printer.println(it) }

    val t = readLine().toInt()
    for (i in 1..t) solveCase(i, readLine, println)
}

private fun solveCase(t: Int, readLine: () -> String, println: (String) -> Unit) {
    val (_, a, b) = readLine().split(" ").map { it.toInt() }
    val u = readLine().split(" ").asSequence().map { it.toInt() }
        .withIndex()
        .filter { it.value > 0 }
        .associate { Pair(it.index + 1, it.value) }

    for (result in 1..402) {
        val d = u.toMutableMap()
        val h = mapOf(result to 1).toMutableMap()

        val intersection = h.keys.intersect(d.keys)
        intersection.forEach { key ->
            remove(key, h, d)
        }

        while (h.isNotEmpty() && d.isNotEmpty()) {
            val (i, c) = h.maxByOrNull { it.value }!!
            h.remove(i)
            arrayOf(i - a, i - b)
                .filter { it > 0 }
                .forEach { ni ->
                    h.merge(ni, c, Int::plus)
                    remove(ni, h, d)
                }
        }

        if (d.isEmpty()) {
            println("Case #$t: $result")
            return
        }
    }

    println("Case #$t: IMPOSSIBLE")
}

private fun remove(key: Int, h: MutableMap<Int, Int>, d: MutableMap<Int, Int>) {
    val hval = h[key] ?: 0
    val dval = d[key] ?: 0
    when {
        hval == dval -> {
            d.remove(key)
            h.remove(key)
        }
        hval < dval -> {
            h.remove(key)
            d[key] = dval - hval
        }
        hval > dval -> {
            d.remove(key)
            h[key] = hval - dval
        }
    }
}
