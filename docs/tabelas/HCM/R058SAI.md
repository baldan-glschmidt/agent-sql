# R058SAI

## Descrição

Saídas de Sinais de Alarme do Coletor

---

## Resumo

- Campos: 13
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPlt | Number(005,0) | Sim | Código do Site |
| CodRlg | Number(005,0) | Sim | Código do Coletor |
| EndSai | Number(003,0) | Sim | Endereço da Saída no Coletor |
| DesSai | String(099) | Sim | Descrição da Saída do Coletor |
| TipSac | Number(001,0) | Sim | Tip. Saída do Coletor |
| NumAmb | Number(009,0) | Sim | Ambiente da Planta |
| CodPlf | Number(007,0) | Sim | Código do Local Físico |
| VerPlf | Number(003,0) | Sim | Versão do Plano de Localização Física |
| CodDsp | Number(009,0) | Não | Código do Dispositivo |
| EndCom | Number(003,0) | Sim | Endereço de Comunicação |
| CodSaa | Number(003,0) | Sim | Código da Interface de Saída |
| EstDef | Number(001,0) | Sim | Estado default |
| UsaPla | String(001) | Sim | Usa Placa Controladora |

---

## Chave Primária

- CodDsp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
