use proselint_registry::checks::{Check, types::*, Padding};

pub const EXAMPLES_PASS: &[&str] = &["Smoke phrase with nothing flagged."];
pub const EXAMPLES_FAIL: &[&str] = &["This leaves much to be desired."];

const CHECK: Check = Check {
	check_type: &Existence {
		items: &[
			"a not unjustifiable assumption",
			"leaves much to be desired",
			"would serve no purpose",
			"a consideration which we should do well to bear in mind",
		],
		padding: Padding::WordsInText,
		exceptions: &[],
	},
	path: "misc.debased",
	msg: "Debased language is a continuous temptation.",
	..Check::default()
};

pub const REGISTER: &[Check] = &[CHECK];
