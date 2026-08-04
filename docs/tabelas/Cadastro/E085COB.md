# E085COB

## Descrição

Cadastros - Clientes - Endereços de Cobrança

---

## Resumo

- Campos: 21
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCli | Number(009,0) | Não | Código do Cliente |
| SeqCob | Number(005,0) | Não | Sequência de endereços de cobrança |
| EndCob | String(100) | Não | Endereço de cobrança do cliente |
| CplCob | String(200) | Sim | Complemento do endereço de cobrança do cliente |
| CepCob | Number(008,0) | Sim | CEP do endereço de cobrança do cliente |
| IniCob | Number(008,0) | Sim | Faixa inicial do CEP do endereço de cobrança do cliente |
| CidCob | String(060) | Sim | Cidade do endereço de cobrança do cliente |
| EstCob | String(002) | Sim | Estado do endereço de cobrança do cliente |
| CgcCob | Number(014,0) | Sim | Número do CNPJ de cobrança |
| DocIdeCob | String(014) | Sim | Número do CNPJ de cobrança |
| BaiCob | String(075) | Sim | Bairro de cobrança do cliente |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o palm |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o Palm |
| SitReg | String(001) | Sim | Situação do registro |
| EenCob | String(018) | Sim | Código do endereço de cobrança do cliente |
| NenCob | String(060) | Sim | Número do Endereço de Cobrança do Cliente |
| FaxCob | String(020) | Sim | Número do fax de contato no endereço de cobrança |
| FonCob | String(020) | Sim | Número do telefone de contato no endereço de cobrança |
| CelCob | String(020) | Sim | Número do telefone celular de contato no endereco de cobrança |
| EmaCob | String(100) | Sim | Endereço eletrônico (E-Mail) contato no endereço de cobrança |

---

## Chave Primária

- CodCli
- SeqCob

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E085COB_000

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |

