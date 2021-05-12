let arr = [2, 4, 6, 20, -1, 1, 39, 20, 1];

arr.sort((a, b) => {
    if(a < b) return 1;
    else if(a == b) return 0;
    else return -1;
});

console.log(arr);

const INIT_VALUE = -1;
const EOW = "\n";
let string_bank = "abcdefghijklmnopqrstuvwxyz" + EOW;

function make_node() {
    let arr = [];
    for(var i = 0; i < string_bank.length; i++) {
        arr.push(INIT_VALUE);
    }

    return arr;
}

function make_trie(trie_root, word) {
    let now = trie_root;
    for(var i = 0; i < word.length; i++) {
        var now_index = string_bank.indexOf(word[i]);
        if(now[now_index] == INIT_VALUE) now[now_index] = make_node();
        now = now[now_index];
    }
}

function search_trie(trie_root, word) {
    let now = trie_root;
    for(var i = 0; i < word.length; i++) {
        var now_index = string_bank.indexOf(word[i]);
        if(now[now_index] == INIT_VALUE) return false;
        now = now[now_index];
    }

    for(var i = 0; i < now.length; i++) {
        if(now[i] != -1) return false;
    }
    
    return true;
}

let trie_root = make_node();

make_trie(trie_root, "asdf" + EOW);
make_trie(trie_root, "aseq" + EOW);
make_trie(trie_root, "efgq" + EOW);
make_trie(trie_root, "asdfq" + EOW);
make_trie(trie_root, "aaaa" + EOW);

console.log(trie_root);

console.log(search_trie(trie_root, "asdf" + EOW));
console.log(search_trie(trie_root, "asdfq" + EOW));
console.log(search_trie(trie_root, "asd" + EOW));

let data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
data.splice(1, 0, 3);
data.splice(1, 1, [2, 4, 0])

console.log(data.findIndex((el) => {
    return el * 2 > 10;
}));

console.log(data);


