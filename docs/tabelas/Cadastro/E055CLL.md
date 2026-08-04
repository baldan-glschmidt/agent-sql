# E055CLL

## Descrição

Cadastro - Tributos - Contas Lalur e Lacs

---

## Resumo

- Campos: 21
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodImp | String(003) | Não | Código do imposto |
| CodCon | String(040) | Não | Código da Conta |
| DesCon | String(250) | Não | Descrição da conta |
| DatCri | Date | Não | Data de criação da conta |
| TipTds | String(004) | Sim | Tipo da Tabela Dinâmica |
| EspTds | String(001) | Sim | Indica a especialização da tabela dinâmica |
| CodLin | String(010) | Sim | Código da linha da tabela dinâmica |
| NumCgc | Number(014,0) | Sim | Número do CNPJ do cliente |
| DocIdeCli | String(014) | Sim | Número do CNPJ do cliente |
| DatLim | Date | Sim | Data Limite para uso do saldo da Conta |
| SalIni | Number(017,2) | Sim | Saldo inicial da conta |
| CodPre | String(001) | Sim | Conta Prejuízo |
| CodPad | String(050) | Sim | Código Padrão Parte B |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodEmp
- CodFil
- CodImp
- CodCon

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
