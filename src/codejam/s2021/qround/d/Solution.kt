package codejam.s2021.qround.d

fun main() {
    val (t, n, q) = readLine()!!.split(" ").map { it.toInt() }
    for (i in 1..t) solveCase(i, n, q)
}

private fun solveCase(t: Int, n: Int, q: Int) {
    val sorted = sort((1..n).toList())

    println(sorted.joinToString(" "))
    readLine()
}

private fun sort(list: List<Int>): List<Int> {
    val nums = list.subList(0, 3)
    println(write(nums))
    val y = readLine()!!.toInt()
    val x = nums.find { it != y }!!
    val z = nums.find { it != y && it != x }!!

    val betweenXY = emptyList<Int>().toMutableList()
    val beforeX = emptyList<Int>().toMutableList()
    val afterY = emptyList<Int>().toMutableList()
    for (i in list.subList(3, list.size)) {
        println(write(listOf(x, y, i)))
        val r = readLine()!!.toInt()
        if (r == i) {
            betweenXY.add(i)
        } else if (r == x) {
            beforeX.add(i)
        } else if (r == y) {
            afterY.add(i)
        }
    }
    afterY.add(z)

    return sort(beforeX, x) + x + sort(betweenXY, y) + y + sort(afterY, y).reversed()
}

private fun sort(list: MutableList<Int>, last: Int): MutableList<Int> {
    val sorted = emptyList<Int>().toMutableList()

    while (list.size > 1) {
        val beforeX2 = list.filter { true }.toMutableList()
        while (beforeX2.size > 1) {
            val (a, b) = beforeX2
            println(write(listOf(a, b, last)))
            val r = readLine()!!.toInt()
            beforeX2.remove(r)
        }
        sorted += beforeX2[0]
        list.remove(beforeX2[0])
    }
    if (list.size == 1) {
        sorted += list[0]
    }
    return sorted
}

private fun write(nums: List<Int>) = nums.joinToString(" ")

