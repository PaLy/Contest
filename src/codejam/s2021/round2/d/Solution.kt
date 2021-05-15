package codejam.s2021.round2.d

import java.io.BufferedReader
import java.io.InputStream
import java.io.InputStreamReader
import java.io.PrintStream
import kotlin.collections.ArrayDeque
import kotlin.collections.HashSet

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
    val (r, c, f, s) = readLine().split(" ").map { it.toInt() }
    var cur = emptyArray<CharArray>().toMutableList()
    val res = emptyArray<CharArray>().toMutableList()
    for (i in 1..r) {
        cur.add(readLine().toCharArray())
    }
    for (i in 1..r) {
        res.add(readLine().toCharArray())
    }

    var cost = 0
    for (i in 0 until r) {
        for (j in 0 until c) {
            if (j < c - 1) {
                if (cur[i][j] == res[i][j + 1] && cur[i][j + 1] == res[i][j] && cur[i][j] != cur[i][j + 1]) {
                    cost += 1
                    val n1 = if (cur[i][j] == 'M') 'G' else 'M'
                    val n2 = if (cur[i][j + 1] == 'M') 'G' else 'M'
                    cur[i][j] = n1
                    cur[i][j + 1] = n2
                }
            }
            if (i < r - 1) {
                if (cur[i][j] == res[i + 1][j] && cur[i + 1][j] == res[i][j] && cur[i][j] != cur[i + 1][j]) {
                    cost += 1
                    val n1 = if (cur[i][j] == 'M') 'G' else 'M'
                    val n2 = if (cur[i + 1][j] == 'M') 'G' else 'M'
                    cur[i][j] = n1
                    cur[i + 1][j] = n2
                }
            }
        }
    }
    for (i in 0 until r) {
        for (j in 0 until c) {
            if (cur[i][j] != res[i][j]) {
                cost += 1
            }
        }
    }

    println("Case #$t: $cost")
}
