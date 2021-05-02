package codejam.s2021.round1c.b

import java.io.BufferedReader
import java.io.InputStream
import java.io.InputStreamReader
import java.io.PrintStream
import java.math.BigInteger
import java.util.*
import kotlin.math.pow

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
    val y = readLine()

    var result = "99999999999999999999999999999999";
    val first = "1000000000000000000000000000000000000000";

    val ss = emptyList<BigInteger>().toMutableList()

    for (l in 1..y.length) {
        if (l == 1) {
            ss.addAll((1L..10).map { it.toBigInteger() }.toList())
        } else {
            ss.add(first.substring(0, l).toBigInteger())
            val t = y.substring(0, l).toBigInteger().minus(BigInteger("100"))
            for (x in 0..200) {
                val next = t.plus(BigInteger(x.toString()))
                if (next > BigInteger.ZERO) {
                    ss.add(next)
                }
            }
        }
    }

    for (s in ss) {
        var yy = s.toString()
        var x = s
        while (yy.toBigInteger() <= y.toBigInteger()) {
            x += BigInteger.ONE
            yy += x.toString()
        }
        if (yy.toBigInteger() < result.toBigInteger() && yy.toBigInteger() > s) {
            result = yy
        }
    }

    println("Case #$t: $result")
}
