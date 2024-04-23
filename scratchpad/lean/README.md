# Lean Prover Scratchpad

On Debian 12, I had success installing Lean via `elan`:

```
sudo apt-get install elan
elan default stable
```

This will install `elan` and set up the current stable version (for me in April 2024, this is Lean 3).

To bootstrap a new project, you can use the following command:

```bash
mkdir my_project
cd my_project
leanpkg init my_project
```

To test that Lean is working, create a simple test proof in a file named `test.lean`:

```lean
theorem one_equals_one : 1 = 1 :=
begin
  refl,
end
```

Run the script to verify the proof.

```bash
lean test.lean
```

The output will be blank if the proof is valid. To test an invalid proof, try the following invalid revision of the previous proof:

```lean
theorem one_equals_one : 1 = 2 :=
begin
  refl,
end
```

You will see errors when attempting to run this script since the proof is not valid.

### Notes

* `leanpkg init` is opinionated about project structure and version management.
  - It will create a git repository in the initialized project. This might be confusing if you are already in a repository. Simply delete the `.git` directory it creates if you require additional flexibility.
  - It will move your lean files into a `src` directory if scripts already exist. I recommend only running `leanpkg init` in a new, empty directory.
