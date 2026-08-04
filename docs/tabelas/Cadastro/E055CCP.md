# E055CCP

## Descrição

Cadastros - Tributos - Parâmetro de Configuração da Contribuição Previdenciária

---

## Resumo

- Campos: 5
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodImp | String(003) | Não | Código do imposto |
| DatBas | Date | Não | Data base inicial de validade para apuração do valor base do imposto |
| ConPre | Number(009,0) | Não | Código da contribuição sobre a receita bruta (tabela 5.1.1 SPED Contribuições) |

---

## Chave Primária

- CodEmp
- CodFil
- CodImp
- DatBas
- ConPre

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E055CCP_002

**Tabela:** E055PAR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodImp | CodImp |

