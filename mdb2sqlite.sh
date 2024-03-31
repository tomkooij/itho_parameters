#!/bin/bash
# from: https://gist.github.com/kazlauskis/1d0bdb9efb3b1bb1e76d48aa368f3a64
# Inspired by 
# https://www.codeenigma.com/community/blog/using-mdbtools-nix-convert-microsoft-access-mysql

# USAGE
# Make sure "mdbtools" is installed
# Rename your MDB file to migration-export.mdb 
# run ./mdb2sqlite.sh migration-export.mdb
# wait and wait a bit longer...

now=$(date +%s)
sqlite=sqlite3
fname=$1
sql=${fname/mdb/sqlite}
schema=${fname/mdb/schema}
dir=${fname/.mdb/}-$now

# Create temporary directory for exported tables
mkdir $dir

# Export database schema from mdb file
mdb-schema $fname sqlite > $dir/$schema

# Export each table in mdb file to temporary sql file
for i in $( mdb-tables $fname ); do 
  echo $i  
  mdb-export -D "%Y-%m-%d %H:%M:%S" -H -q "'" -I sqlite $fname $i > $dir/$i.sql
done

# Create destination sqlite database based on previously exported schema
< $dir/$schema $sqlite $sql

# Insert values from temporary exported tables into destination database
for f in $dir/*.sql ; do 
  echo $f 
  (echo 'BEGIN;'; cat $f; echo 'COMMIT;') | $sqlite $sql
done
echo "Using $dir"
