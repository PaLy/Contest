package codejam.s2022.round1b.b

import java.io.BufferedReader
import java.io.InputStream
import java.io.InputStreamReader
import java.io.PrintStream
import kotlin.math.abs

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
    val (n, p) = readLine().split(" ").map { it.toInt() }
    val x = (0 until n).map {
        readLine().split(" ").map { it.toLong() }.sorted()
    }

    val d = (0 until n).map {
        (0 until 2).map { Long.MAX_VALUE }.toMutableList()
    }

    for (i in x.indices) {
        val xx = x[i]
        if (i == 0) {
            d[0][0] = xx.last() + xx.last() - xx.first()
            d[0][1] = xx.last()
        } else {
            val prevx = x[i - 1]

            d[i][0] = minOf(
                d[i - 1][0] + abs(xx.last() - prevx.first()) + xx.last() - xx.first(),
                d[i - 1][1] + abs(xx.last() - prevx.last()) + xx.last() - xx.first()
            )
            d[i][1] = minOf(
                d[i - 1][0] + abs(xx.first() - prevx.first()) + xx.last() - xx.first(),
                d[i - 1][1] + abs(xx.first() - prevx.last()) + xx.last() - xx.first()
            )
        }
    }

    println("Case #${t}: ${d.last().minOrNull()}")
}
