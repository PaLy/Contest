package codejam.s2021.round1c.c

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
    val (s, e) = readLine().split(" ")

    val queue = ArrayDeque<Pair<Int, String>>()
    queue.add(Pair(0, s))

    var steps = 0
    var result = 0
    val was = HashSet<String>()

    while (!queue.isEmpty()) {
        if (steps == 75000) {
            println("Case #$t: IMPOSSIBLE")
            return
        } else {
            val (d, c) = queue.removeFirst()
            if (c == e) {
                result = d
                break
            } else {
                if (c != "0") {
                    val cDoubled = c + "0"
                    if (!was.contains(cDoubled)) {
                        was.add(cDoubled)
                        queue.add(Pair(d + 1, cDoubled))
                    }
                }
                val cNegated = negate(c)
                if (!was.contains(cNegated)) {
                    was.add(cNegated)
                    queue.add(Pair(d + 1, cNegated))
                }
            }
            steps += 1
        }
    }

    println("Case #$t: $result")
}

fun negate(c: String): String {
    var result = c
        .replace('0', '2')
        .replace('1', '0')
        .replace('2', '1')
    val beginning = result.indexOf('1')
    if (beginning == -1) {
        return "0"
    } else {
        return result.substring(beginning)
    }
}
