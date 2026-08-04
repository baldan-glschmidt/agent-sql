# E000ROC

## Descrição

Tabelas - Integrações - Retornos de Integração - Ligação Ordem de Compra

---

## Resumo

- Campos: 6
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqRip | Number(009,0) | Não | Número sequencial dos registros de retorno da integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumOcp | Number(008,0) | Não | Número da ordem de compra |
| SitRet | String(001) | Sim | Situação do retorno da Ordem de Compra A - Aprovação R - Recusado I - Inconsistência C - Cancelado F - Erro ao inserir fornecedor M - Aguardando aprovação ERP |
| MsgRet | String(255) | Sim | Mensagem explicativa do retorno do envio |

---

## Chave Primária

- SeqRip

---

## Índices

### E000ROCIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- NumOcp

---

## Relacionamentos

### IR_E000ROC_000

**Tabela:** E000RIP

| Origem | Destino |
|--------|---------|
| SeqRip | SeqRip |

