# E000NFS

## Descrição

Tabelas - Integrações - Notas fiscais de saída

---

## Resumo

- Campos: 6
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqInt | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| RegApu | String(001) | Sim | Indica se a nota foi apurada pela controladoria |

---

## Chave Primária

- SeqInt

---

## Índices

### E000NFSIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodSnf
- NumNfv

---

## Relacionamentos

Nenhum relacionamento cadastrado.
