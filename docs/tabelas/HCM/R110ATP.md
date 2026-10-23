# R110ATP

## Descrição

Aceite do Termo de Consentimento - Paciente

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFic | Number(009,0) | Não | Código Ficha Médica |
| TipTer | Number(001,0) | Não | Tipo do termo de consentimento |
| CodVer | Number(004,0) | Não | Código da versão do termo de consentimento |
| DatAce | Date | Sim | Data que paciente aceitou a versão do termo de consentimento |
| DatRev | Date | Sim | Data que paciente revogou a versão do termo de consentimento |
| NomArq | String(250) | Sim | Nome do arquivo anexado |
| AneCon | Image | Sim | Arquivo anexo do termo de consentimento |
| ConTra | String(001) | Sim | Consentimento aceito no Contrato de Trabalho |

---

## Chave Primária

- NumEmp
- CodFic
- TipTer
- CodVer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
