# Anki production note schema

We use a custom Anki note type named `Castellano Production` for managed English-to-Spanish production cards. Version 1 uses fields in this order: `CardKey`, `Prompt`, `Answer`, `Extra`, `Source`, `LexicalKey`; `CardKey` is first because Anki uses the first field for duplicate and import matching, and it provides stable sync identity without storing Anki note or card ids in the learning repo.

When syncing, the tutor searches for `note:"Castellano Production" CardKey:<key>`: zero matches creates a note, one match updates fields, and more than one match is treated as a duplicate error rather than being auto-fixed. Tags are maintained for filtering and grouping only, with the v1 managed tags `castellano`, `castellano::managed`, `castellano::production`, `castellano::lesson::001`, and `castellano::schema::v1`; prompt text, answer text, and tags are not identity because they can be edited, deleted, or renamed.
