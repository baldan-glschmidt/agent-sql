# R150GRC

## Descrição

Grupos - Condições

---

## Resumo

- Campos: 7
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodGru | Number(004,0) | Não | Código do Grupo |
| DatRef | Date | Não | Data de Referência da Condição |
| SeqCon | Number(002,0) | Não | Sequência da Condição |
| AbrEmp | String(100) | Sim | Abrangência de Empresa |
| AbrFil | String(100) | Sim | Abrangência de Filial |
| AbrCcu | String(200) | Sim | Abrangência de Centro de Custo |
| AbrLoc | String(1500) | Sim | Abrangência de Local |

---

## Chave Primária

- CodGru
- DatRef
- SeqCon

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R150GRC_000

**Tabela:** R150GRU

| Origem | Destino |
|--------|---------|
| CodGru | CodGru |

