package codejam.s2022.round2.c

import java.io.BufferedReader
import java.io.InputStream
import java.io.InputStreamReader
import java.io.PrintStream
import kotlin.math.sqrt

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
    val cx = Array(n) {0}
    val cy = Array(n) {0}
    val sx = Array(n + 1) {0}
    val sy = Array(n + 1) {0}
    for (i in 0 until n) {
        val (x, y) = readLine().split(" ").map { it.toInt() }
        cx[i] = x
        cy[i] = y
    }
    for (i in 0 .. n) {
        val (x, y) = readLine().split(" ").map { it.toInt() }
        sx[i] = x
        sy[i] = y
    }

    val cleft = emptyList<Int>().toMutableList()
    val sleft = emptyList<Int>().toMutableList()
    for (i in 0 until n) {
        cleft.add(i)
    }
    for (i in 0 .. n) {
        sleft.add(i)
    }

    val result = if (next(cleft, sleft, cx, cy, sx, sy, n)) {
        "POSSIBLE"
    } else {
        "IMPOSSIBLE"
    }

    println("Case #${t}: $result")
}

fun next(
    cleft: List<Int>,
    sleft: List<Int>,
    cx: Array<Int>,
    cy: Array<Int>,
    sx: Array<Int>,
    sy: Array<Int>,
    n: Int
): Boolean {
    if (cleft.isEmpty()) {
        return sleft.contains(0)
    } else {
        for (ci in cleft) {
            var bestSi = emptyList<Int>().toMutableList()
            var bestD = Double.MAX_VALUE
            for (si in sleft) {
                val dx = cx[ci].toDouble() - sx[si]
                val dy = cy[ci] - sy[si]
                val d = sqrt(dx * dx + dy * dy)
                if (d < bestD) {
                    bestD = d
                    bestSi = emptyList<Int>().toMutableList()
                }
                if (d <= bestD) {
                    bestSi.add(si)
                }
            }

            // TODO how to choose from multiple bestSi

            val ncleft = cleft.filter { it != ci }
            val nsleft = sleft.filter { it != bestSi.first() }
            if (next(ncleft, nsleft, cx, cy, sx, sy, n)) {
                return true
            }
        }
        return false
    }
}
