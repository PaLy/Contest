package codejam.s2022.round1a.b

import java.io.BufferedReader
import java.io.InputStream
import java.io.InputStreamReader
import java.io.PrintStream

fun main() {
    solve(System.`in`, System.out)
}

fun solve(inputStream: InputStream, out: PrintStream) {
    val reader = BufferedReader(InputStreamReader(inputStream))
    val printer = PrintStream(out)
    val readLine = { reader.readLine() }
    val println = { it: String ->
        printer.println(it)
        printer.flush()
    }

    val t = readLine().toInt()
    for (i in 1..t) solveCase(i, readLine, println)
}

private fun solveCase(t: Int, readLine: () -> String, println: (String) -> Unit) {
    val n = readLine().toInt()

    val a1 = emptyList<Long>().toMutableList()
    var x = 1L
    while (true) {
        a1.add(x)
        x *= 2
        if (x > 1000000000) break
    }
    val a2 = listOf(1025L).toMutableList()
    while (a1.size + a2.size < n) {
        a2.add(a2.last() + 1)
    }
    println((a1 + a2).joinToString(" "))

    val b = readLine().split(" ").map { it.toLong() }

    val s1 = emptyList<Long>().toMutableList()
    val s2 = emptyList<Long>().toMutableList()

    (a2 + b + a1.reversed()).forEach {
        if (s1.sum() <= s2.sum()) {
            s1.add(it)
        } else {
            s2.add(it)
        }
    }

    println(s1.joinToString(" "))
}
