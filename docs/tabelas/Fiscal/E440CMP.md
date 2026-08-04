# E440CMP

## Descrição

Compras - Notas Fiscais de Entrada - Manifesto Documento Fiscal - Componentes do Pagamento

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
| CodSma | String(003) | Não | Código da série do manifesto |
| NumMan | Number(009,0) | Não | Número do manifesto |
| SeqCmp | Number(003,0) | Não | Sequência do Componente do Pagamento |
| TipCmp | Number(002,0) | Sim | Tipo do Componente |
| VlrCmp | Number(015,2) | Sim | Valor do componente |
| DesCmp | String(060) | Sim | Descrição do componente do tipo Outros |

---

## Chave Primária

- CodEmp
- CodFil
- CodSma
- NumMan
- SeqCmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440CMP_003

**Tabela:** E440MDF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSma | CodSma |
| NumMan | NumMan |

