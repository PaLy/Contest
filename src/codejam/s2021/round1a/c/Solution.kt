package codejam.s2021.round1a.c

import java.io.BufferedReader
import java.io.InputStream
import java.io.InputStreamReader
import java.io.PrintStream
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
    val (n, q) = readLine().split(" ").map { it.toInt() }

    val a = listOf<String>().toMutableList()
    val s = listOf<Int>().toMutableList()
    for (i in 1..n) {
        val (ai, si) = readLine().split(" ")
        a += ai
        s += si.toInt()
    }

    val possibleAnswers = setOf<String>().toMutableList()

    for (mask in 0 until (2.0.pow(q.toDouble()).toInt())) {
        var ms = mask.toString(2)
        while (ms.length < q) ms = "0$ms"
        val answers = ms.map { if (it == '0') 'F' else 'T' }.joinToString("")
        val ok = (0 until n).map { i ->
            val correct = a[i].mapIndexed { i, ai -> answers[i] == ai }.sumOf { if (it) 1L else 0 }.toInt()
            if (correct == s[i]) 1 else 0
        }.sum()
        if (ok == n) {
            possibleAnswers.add(answers)
        }
    }

    var resultAnswers = ""
    var maxScore = 0

    for (mask in 0 until (2.0.pow(q.toDouble()).toInt())) {
        var ms = mask.toString(2)
        while (ms.length < q) ms = "0$ms"
        val myAnswers = ms.map { if (it == '0') 'F' else 'T' }.joinToString("")
        val scoreSum = possibleAnswers.map { answer ->
            answer.mapIndexed { index, c -> c == myAnswers[index] }.sumOf { if (it) 1L else 0 }.toInt()
        }.sum()

        if (scoreSum > maxScore) {
            maxScore = scoreSum
            resultAnswers = myAnswers
        }
    }

    val g = gcd(maxScore, possibleAnswers.size)

    println("Case #$t: $resultAnswers ${maxScore/g}/${possibleAnswers.size/g}")
}


fun gcd(n1: Int, n2: Int): Int {
    return if (n2 != 0)
        gcd(n2, n1 % n2)
    else
        n1
}