# E055PFA

## Descrição

Cadastros - Tributos - Forma de Apuração da Estimativa Mensal

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodImp | String(003) | Não | Código do imposto |
| DatRef | Date | Não | Competência Início |
| FapEme | String(001) | Sim | Forma Apuração |
| VisDre | String(020) | Sim | Código da visão contábil da demonstração do resultado do exercício |
| CtbAut | String(001) | Não | Contabilização Automática |
| SimApu | String(001) | Não | Indica se deseja realizar a simulação da apuração oposta |

---

## Chave Primária

- CodEmp
- CodFil
- CodImp
- DatRef

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E055PFA_002

**Tabela:** E055PAR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodImp | CodImp |

