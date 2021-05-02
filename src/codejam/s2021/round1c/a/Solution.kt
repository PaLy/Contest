package codejam.s2021.round1c.a

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
    val (n, k) = readLine().split(" ").map { it.toInt() }
    val pOrig = readLine().split(" ").map { it.toInt() }
    val p = pOrig.toMutableList()
    p.add(0)
    p.add(k + 1)

    val pSorted = p.sorted().distinct()

    var chosenA = -1
    var chosenB = -1
    var intervalA = 0
    var intervalB = 0
    for (i in 0 until pSorted.size - 1) {
        val interval = if (i == 0 || i == pSorted.size - 2)
            pSorted[i + 1] - pSorted[i] - 1
        else
            (pSorted[i + 1] - pSorted[i]) / 2

        val interval2 = if (i == 0 || i == pSorted.size - 2)
            -1
        else
            (pSorted[i + 1] - pSorted[i] - 1) / 2

        if (interval > intervalA) {
            intervalB = intervalA
            chosenB = chosenA
            intervalA = interval
            chosenA = pSorted[i] + 1
            if (chosenA == 0) {
                chosenA = pSorted[i + 1] - 1
            }
            if (chosenA == k + 1) {
                chosenA = pSorted[i]
            }
        } else if (interval > intervalB) {
            intervalB = interval
            chosenB = pSorted[i] + 1
            if (chosenB == 0) {
                chosenB = pSorted[i + 1] - 1
            }
            if (chosenB == k + 1) {
                chosenB = pSorted[i]
            }
        }

        if (interval2 > -1) {
            if (interval2 > intervalA) {
                intervalB = intervalA
                chosenB = chosenA
                intervalA = interval2
                chosenA = pSorted[i + 1] - 1
            } else if (interval2 > intervalB) {
                intervalB = interval2
                chosenB = pSorted[i + 1] - 1
            }
        }
    }

    val result = if (chosenA != chosenB) (intervalA + intervalB) / (1.0 * k) else (intervalA) / (1.0 * k)

    println("Case #$t: $result")
}