-- This module serves as the root of the `LeanTest` library.
-- Import modules here that should be built as part of the library.
import «LeanTest».Basic
import Mathlib.Data.Set.Basic

theorem one_equals_one : 1 = 1 := by
  rfl

example (x : U) (A : Set U) (h : x ∈ A) : x ∈ A := by
  exact h
