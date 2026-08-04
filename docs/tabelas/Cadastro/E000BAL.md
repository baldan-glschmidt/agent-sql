# E000BAL

## Descrição

Cadastro de Definições de Leitura da Balança

---

## Resumo

- Campos: 12
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodUsu | Number(010,0) | Não | Identificador do usuário |
| PrtBal | Number(001,0) | Sim | Porta Serial de Comunicação |
| CntBal | Number(001,0) | Sim | Conector da Comunicação |
| SclBal | Number(005,0) | Sim | Identificação da Balança |
| ChnBal | Number(001,0) | Sim | Canal de Comunicação |
| TipEnt | Number(001,0) | Sim | Tipo de Pesagem na Entrada |
| TipSai | Number(001,0) | Sim | Tipo de Pesagem na Saída |
| DllBal | String(050) | Sim | Nome da DLL |
| TipDll | Number(001,0) | Sim | Tipo da DLL |
| UrlEnt | String(250) | Sim | URL do serviço de captura de peso da Balança de entrada |
| UrlSai | String(250) | Sim | URL do serviço de captura de peso da Balança de saída |

---

## Chave Primária

- CodEmp
- CodUsu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
