# R303DPC

## Descrição

e-Sfinge - Concursos / Desistência da Posse

---

## Resumo

- Campos: 11
- Chave Primária: 9 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| AnoBas | Number(004,0) | Não | Ano |
| BimAno | Number(001,0) | Não | Código Bimestre Ano |
| Edital | String(016) | Não | Número do edital de concurso |
| Especi | Number(006,0) | Não | Número da especialidade |
| NumIns | Number(016,0) | Não | Número de inscrição do candidato no concurso |
| TipQua | Number(002,0) | Não | Tipo de Quadro |
| CodCar | String(016) | Não | Código do Cargo |
| VigCar | Date | Não | Data de Início da Vigência do Cargo |
| DatDes | Date | Não | Data em que o participante desistiu de tomar posse no cargo |
| OriReg | String(001) | Sim | Origem do Registro (G-Gerado, D-Digitado, I-Importado) |

---

## Chave Primária

- NumEmp
- AnoBas
- BimAno
- Edital
- Especi
- NumIns
- TipQua
- CodCar
- VigCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
