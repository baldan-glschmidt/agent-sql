# E000RMO

## Descrição

Tabelas - Integrações - Ordem de Compra - Recebimento de Mercadoria

---

## Resumo

- Campos: 14
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
| NumOcp | Number(008,0) | Não | Número da ordem de compra |
| SeqIpo | Number(004,0) | Sim | Sequência de item da ordem de compra |
| SeqIso | Number(004,0) | Sim | Sequência do item de serviço na ordem de compra |
| EmpNfc | Number(004,0) | Não | Código da empresa |
| FilNfc | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do Fornecedor |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal |
| QtdRec | Number(014,5) | Sim | Quantidade recebida do produto da ordem de compra |
| FlgFec | String(001) | Não | Indica se a ordem de compra foi finalizada |
| SeqCan | Number(009,0) | Sim | Número sequencial do registro que efetuou o cancelamento deste registro |

---

## Chave Primária

- SeqInt

---

## Índices

### E000RMOIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- NumOcp
- SeqIpo

---

## Relacionamentos

Nenhum relacionamento cadastrado.
