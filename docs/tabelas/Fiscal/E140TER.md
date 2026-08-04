# E140TER

## Descrição

Vendas - Notas Fiscais de Saída - Itens de Produtos - Terminais Adicionais NFCom

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqTer | Number(004,0) | Não | Sequencial |
| NumTer | String(012) | Sim | Número do terminal adicional |
| UfsTer | String(002) | Sim | Sigla do estado |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqTer

---

## Índices

### E140TERIndice1

**Tipo:** Não unico

Campos:
- CodEmp

---

## Relacionamentos

Nenhum relacionamento cadastrado.
