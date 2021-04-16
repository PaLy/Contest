package codejam.s2021.qround.c

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
    val println = { it: String -> printer.println(it) }

    val t = readLine().toInt()
    for (i in 1..t) solveCase(i, readLine, println)
}

private fun solveCase(t: Int, readLine: () -> String, println: (String) -> Unit) {
    val (n, c) = readLine().split(" ").map { it.toInt() }

    val max = n * (n + 1) / 2 - 1
    val min = n - 1

    val a = if (c > max || c < min) {
        emptyList()
    } else {
        var a = (1..n).toList()
        var toSave = max - c

        for (i in n - 2 downTo 0) {
            val maxCost = n - i
            val save = arrayOf(toSave, maxCost - 1).minOrNull()!!
            val cost = maxCost - save

            a = a.subList(0, i) + a.subList(i, i + cost).asReversed() + a.subList(i + cost, n)

            toSave -= save
        }

        a
    }

    if (a.isEmpty()) {
        println("Case #$t: IMPOSSIBLE")
    } else {
        println("Case #$t: ${a.joinToString(" ")}")
    }
}
