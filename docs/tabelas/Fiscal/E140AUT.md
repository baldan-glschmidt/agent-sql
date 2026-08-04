# E140AUT

## Descrição

Vendas - Notas Fiscais de Saída - Dados Gerais - Autorizados Download XML

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqAut | Number(004,0) | Não | Sequência das pessoas autorizadas a baixar o XML |
| TipCli | String(001) | Não | Tipo do cliente |
| CgcCpf | Number(014,0) | Sim | Número do CNPJ ou CPF do cliente |
| DocIde | String(014) | Sim | Número do CNPJ ou CPF do cliente |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqAut

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140AUT_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

