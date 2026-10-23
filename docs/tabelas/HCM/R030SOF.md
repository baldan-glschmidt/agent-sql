# R030SOF

## Descrição

eSocial - Software House

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodOem | Number(008,0) | Não | Código da Empresa de Sofware (Outras empresas) |
| DatIni | Date | Não | Competência de início |
| NomCon | String(070) | Sim | Nome do contato na empresa |

---

## Chave Primária

- NumEmp
- CodOem
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030SOF_001

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

