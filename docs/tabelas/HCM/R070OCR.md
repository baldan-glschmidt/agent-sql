# R070OCR

## Descrição

Colaboradores Outras Unidades

---

## Resumo

- Campos: 20
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador de Outra Unidade |
| NomCra | String(040) | Sim | Nome no Crachá do Colaborador de Outra Unidade |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Local do Organograma |
| CodPrm | Number(005,0) | Sim | Código da Permissão de Acesso |
| PrmFer | Number(005,0) | Sim | Permissão de Acesso para os Feriados |
| PrmSab | Number(005,0) | Sim | Permissão de Acesso para os Sábados |
| PrmDom | Number(005,0) | Sim | Permissão de Acesso para os Domingos |
| AceOcr | Number(001,0) | Sim | Status de Acesso do Colaborador de Outra Unidade |
| EmpOri | Number(004,0) | Sim | Código da Empresa de Origem do Colaborador de Outra Unidade |
| FilOri | Number(006,0) | Sim | Código da Filial de Origem do Colaborador de Outra Unidade |
| CodEsc | Number(009,0) | Sim | Código da Escala |
| CodTma | Number(001,0) | Sim | Código da Turma da Escala |
| ConFai | Number(001,0) | Sim | Controla Faixa Horária de Acesso |
| FotOcr | Image | Sim | Foto do Colaborador de Outra Unidade |
| UtiChv | String(001) | Sim | Pode usar chave |
| DatFot | Date | Sim | Data da Foto |
| HorFot | Number(005,0) | Sim | Hora da Foto |
| UsaRFa | String(001) | Sim | Utiliza Reconhecimento Facial |

---

## Chave Primária

- NumEmp
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
