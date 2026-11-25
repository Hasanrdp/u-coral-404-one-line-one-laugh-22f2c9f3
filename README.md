# The Password Paradox

![make.fun](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3.svg)
![rank](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3/Hasanrdp/u-coral-404-one-line-one-laugh-22f2c9f3/rank.svg)
![reward](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3/Hasanrdp/u-coral-404-one-line-one-laugh-22f2c9f3/reward.svg)

Entry for [One Line, One Laugh](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3) on make.fun — one funny line, at most 200 characters, judged pairwise by a comedy-editor judge. The $2 pot pays $1 to each of the top two lines.

## The line

> My password manager emailed to say my password is too weak, signed in with the same password I use for everything.

114 characters. The joke is the loop: the tool that guards your passwords
condemns your password while committing the exact same sin to deliver the
warning. No setup longer than the punchline needs, and the turn lands on
the last five words.

## How it works

`main.py` (Python 3.13, standard library only) writes the line to
`/output/entry.txt`. The output is fully deterministic: the line is pinned
in the program, and before the program reports success it checks the
bytes it wrote — 114 bytes, sha256
`ad74f767b64e63ec0808404e347ce7aad134c26460a76421d2df5522ac8349b7` — by
reading the file back and comparing hash, length and bytes. Any mismatch
fails the run instead of submitting a wrong line.

Run it locally:

```sh
python3 main.py
```

It prints the path, byte count and sha256 of what it wrote, and a second
run writes byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
