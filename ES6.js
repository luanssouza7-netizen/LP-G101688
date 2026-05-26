// CRIANDO UM VETOR
const vetorNumeros = [10, 20, 30, 40, 50]

console.log("Listando todos os elementos do vetor:")
console.log(vetorNumeros)

console.log("\n Filtrado cada elemento pares:")
vetorNumeros.push(8)
vetorNumeros.push(142)
const pares = vetorNumeros.map(n => n * 2)
console.log(pares)

console.log("\n Filtrado cada elemento impares:")
vetorNumeros.push(1)
vetorNumeros.push(3)
const impares= vetorNumeros.filter(n => n * 2)
console.log(impares)

console.log("\n Filtrando elemento negativo")
vetorNumeros.push(-1)
vetorNumeros.push(-89)
const negativo = vetorNumeros.filter(n => n < 0)
console.log(negativo)


