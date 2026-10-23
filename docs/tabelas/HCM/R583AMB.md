# R583AMB

## Descrição

Cadastro de Ambientes

---

## Resumo

- Campos: 12
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumAmb | Number(007,0) | Não | Código do Ambiente de Trabalho |
| NomAmb | String(100) | Sim | Nome do Ambiente |
| LocAmb | Number(001,0) | Sim | Localização do Ambiente |
| EmpAmb | Number(004,0) | Sim | Código da Empresa do Ambiente |
| FilAmb | Number(006,0) | Sim | Código da Filial do Ambiente |
| OemAmb | Number(008,0) | Sim | Código da Outra Empresa do Ambiente |
| TipIns | Number(001,0) | Sim | Tipo de inscrição do estabelecimento onde está localizado o ambiente |
| NumIns | Number(015,0) | Sim | Número de inscrição do estabelecimento onde está localizado o ambiente - Obsoleto |
| CfjIns | String(014) | Sim | Número de inscrição do estabelecimento onde está localizado o ambiente |
| VerPlf | Number(003,0) | Sim | Versão do Plano de Localização Física |
| CodPlf | Number(007,0) | Sim | Código do Local Físico do Ambiente |
| CodLot | String(030) | Sim | Código atribuído pela empresa para a lotação tributária |

---

## Chave Primária

- NumAmb

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
