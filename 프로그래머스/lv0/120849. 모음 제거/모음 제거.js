const vowels = ['a', 'e', 'i', 'o', 'u']

function solution(my_string) {
    vowels.forEach(vowel => {
        my_string = my_string.replaceAll(vowel, '')    
    })
    
    return my_string
}