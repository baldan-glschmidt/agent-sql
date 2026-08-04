# E000NFD

## Descrição

Tabelas - Integrações - Item nota fiscal de saída

---

## Resumo

- Campos: 7
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
| SeqIpv | Number(003,0) | Sim | Sequência do item na nota fiscal de saída |
| SeqIsv | Number(003,0) | Sim | Sequência do item na nota fiscal de saída |

---

## Chave Primária

- SeqInt

---

## Índices

### E000NFDIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqIpv
- SeqIsv

---

## Relacionamentos

Nenhum relacionamento cadastrado.
