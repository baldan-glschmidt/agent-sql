# R088CVT

## Descrição

Condutores de Veículos de Teste

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
| EmpCon | Number(004,0) | Não | Código da Empresa do Condutor |
| TClCon | Number(001,0) | Não | Tipo de Colaborador Condutor |
| CadCon | Number(009,0) | Não | Cadastro do Condutor |
| DatIna | Date | Sim | Data de Inatividade |

---

## Chave Primária

- EmpCon
- TClCon
- CadCon

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088CVT_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| EmpCon | NumEmp |
| TClCon | TipCol |
| CadCon | NumCad |

