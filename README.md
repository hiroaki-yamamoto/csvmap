# Simple CSV Mapping Script

## What's this?
  This script converts a specific formatted csv into the other formatted csv.

## Use-case
  I made this script to use my business. For example, I purchased something
  to create products, but I paid with the products I created from inventory.
  In this case, making sales invoice and purchase invoice should be
  made/received in 1 time.

## How to use
  First, you will need to create mapping configuration files. You can see the
  example at [here](example).

  As reference, here is the description:

### fieldnames
  A list of the fields. This will be passed `fieldnames` at `csv.DictWriter` of
  Python Standard Library.

### map
  A dictionary of old-field (as key) and new-field (as value). The field that
  is specified here can be transformed into the corresponding field.
  If the field couldn't be found here, the value will be removed or set default
  value at `default_value`.

  Currently, this supports only OneToOne transformation.

### default_value
  If the value is empty (or removed), this default_value is set.

## Contribution
  Issues / PR is acceptable.

## License
  This script is licensed under the terms of MIT License. For details, please
  refer [here](LICENSE.md)
