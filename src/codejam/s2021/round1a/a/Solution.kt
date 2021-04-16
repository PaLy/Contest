package codejam.s2021.round1a.a

import java.io.BufferedReader
import java.io.InputStream
import java.io.InputStreamReader
import java.io.PrintStream
import java.math.BigInteger
import kotlin.math.min

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
    val n = readLine().toInt()
    val x = readLine().split(" ").map { it.toBigInteger() }

    var last = x[0]
    var cost = 0

    for (i in 1 until n) {
        var cur = x[i]

        if (cur <= last) {
            val curs = cur.toString()
            val lasts = last.toString()
            val len = min(curs.length, lasts.length)
            if (curs.length == lasts.length || curs.substring(0, len) != lasts.substring(0, len)) {
                while (cur <= last) {
                    cur *= BigInteger.valueOf(10)
                    cost += 1
                }
            } else {
                val suffix = lasts.substring(len)
                val suffix1 = suffix.toBigInteger() + BigInteger.ONE
                val suffix1s = suffix1.toString()
                if (suffix1s.length == suffix.length) {
                    cur = (curs + suffix1s).toBigInteger()
                    cost += suffix.length
                } else {
                    while (cur <= last) {
                        cur *= BigInteger.valueOf(10)
                        cost += 1
                    }
                }
            }
        }

        last = cur
    }

    println("Case #$t: $cost")
}
