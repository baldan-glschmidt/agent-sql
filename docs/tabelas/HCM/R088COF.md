# R088COF

## Descrição

Condutores de veículos da frota

---

## Resumo

- Campos: 9
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EmpCon | Number(004,0) | Não | Código da empresa do condutor |
| TClCon | Number(001,0) | Não | Tipo de Colaborador Condutor |
| CadCon | Number(009,0) | Não | Cadastro do Condutor |
| TipDoc | Number(004,0) | Sim | Tipo do Documento |
| NumCnh | String(020) | Sim | Número do documento |
| CatCnh | String(004) | Sim | Categoria da carteira de habilitação |
| DatCnh | Date | Sim | Data da expedição do documento |
| VenCnh | Date | Sim | Data do vencimento do documento |
| SeqDoc | Number(002,0) | Sim | Sequência do Documento |

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

### IR_R088COF_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| EmpCon | NumEmp |
| TClCon | TipCol |
| CadCon | NumCad |

