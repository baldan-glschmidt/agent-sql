# E140MNV

## Descrição

Vendas - Notas Fiscais de Saída - Mensagens

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
| SeqMnv | Number(009,0) | Não | Sequencia |
| CodEmp | Number(004,0) | Não | Código da empresa da nota fiscal de saída |
| CodFil | Number(005,0) | Não | Código da filial da nota fiscal de saída |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| CodMsg | Number(004,0) | Não | Código da mensagem da nota fiscal de saída |
| MsgNfv | String(1000) | Não | Texto da mensagem da nota fiscal de saída |

---

## Chave Primária

- SeqMnv

---

## Índices

### E140MNVNotaFiscal

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodSnf
- NumNfv

---

## Relacionamentos

Nenhum relacionamento cadastrado.
