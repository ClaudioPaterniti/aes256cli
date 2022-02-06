import click
import getpass

import aes256.api.encrypt as encrypt_api
import aes256.api.decrypt as decrypt_api

@click.group('cli')
def cli():
    pass


@cli.command('encrypt')
@click.argument('input_path')
@click.option('--out', '-o', 'output_path')
def cli_encrypt(input_path: str, output_path: str):
    if not output_path:
        output_path = 'aes256encrypted_' + input_path
    key = getpass.getpass('Insert Encryption key: ')
    try:
        encrypt_api.encrypt_file(input_path, key, output_path)
    except:
        print('error')


@cli.command('decrypt')
@click.argument('input_path')
@click.option('--out', '-o', 'output_path')
def cli_decrypt(input_path: str, output_path: str):
    if not output_path:
        output_path = 'aes256decrypted_' + input_path
    key = getpass.getpass('Insert Encryption key: ')
    try:
        decrypt_api.decrypt_file(input_path, key, output_path)
    except:
        print('error')
