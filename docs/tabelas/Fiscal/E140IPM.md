# E140IPM

## Descrição

Vendas - Notas Fiscais de Saída - Itens de Produto - Mensagens

---

## Resumo

- Campos: 8
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqIpm | Number(009,0) | Não | Sequencia |
| CodEmp | Number(004,0) | Não | Código da empresa da nota fiscal de saída |
| CodFil | Number(005,0) | Não | Código da filial da nota fiscal de saída |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqIpv | Number(003,0) | Não | Sequência do item de produto da nota fiscal de saída |
| CodMsg | Number(004,0) | Não | Código da mensagem do item de produto da nota fiscal de saída |
| MsgIpm | String(1000) | Não | Texto da mensagem do item de produto da nota fiscal de saída |

---

## Chave Primária

- SeqIpm

---

## Índices

### E140IPMItemNotaFiscal

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqIpv

---

## Relacionamentos

Nenhum relacionamento cadastrado.
