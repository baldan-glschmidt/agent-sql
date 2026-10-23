# R088ATV

## Descrição

Autorização para Habilitação por Tipo de Veículo

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EmpCon | Number(004,0) | Não | Código da Empresa do Condutor |
| TClCon | Number(001,0) | Não | Tipo de Colaborador Condutor |
| CadCon | Number(009,0) | Não | Cadastro do Condutor |
| TipVei | Number(002,0) | Não | Tipo de Veículo e Espécie Denatran |
| DatVal | Date | Sim | Data da Validade da Autorização |
| CodUsu | Number(010,0) | Sim | Código do Usuário |

---

## Chave Primária

- EmpCon
- TClCon
- CadCon
- TipVei

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088ATV_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| EmpCon | NumEmp |
| TClCon | TipCol |
| CadCon | NumCad |

### IR_R088ATV_003

**Tabela:** R088TPV

| Origem | Destino |
|--------|---------|
| TipVei | TipTpv |

